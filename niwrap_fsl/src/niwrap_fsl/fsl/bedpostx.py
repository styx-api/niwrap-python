# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

BEDPOSTX_METADATA = Metadata(
    id="63953cadd31dba0e63cb83d39dff3c9e3f583e39.boutiques",
    name="bedpostx",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


BedpostxParameters = typing.TypedDict('BedpostxParameters', {
    "__STYXTYPE__": typing.Literal["bedpostx"],
    "subject_dir": str,
    "num_fibres": typing.NotRequired[float | None],
    "ard_weight": typing.NotRequired[float | None],
    "burnin": typing.NotRequired[float | None],
    "num_jumps": typing.NotRequired[float | None],
    "sample_every": typing.NotRequired[float | None],
    "model_type": typing.NotRequired[float | None],
    "grad_nonlinear": bool,
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "bedpostx": bedpostx_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "bedpostx": bedpostx_outputs,
    }.get(t)


class BedpostxOutputs(typing.NamedTuple):
    """
    Output object returned when calling `bedpostx(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    xfms_output: OutputPathType
    """Output transformations."""
    diff_slices_output: OutputPathType
    """Output diffusion slices."""


def bedpostx_params(
    subject_dir: str,
    num_fibres: float | None = 3,
    ard_weight: float | None = 1,
    burnin: float | None = 1000,
    num_jumps: float | None = 1250,
    sample_every: float | None = 25,
    model_type: float | None = 2,
    grad_nonlinear: bool = False,
) -> BedpostxParameters:
    """
    Build parameters.
    
    Args:
        subject_dir: Input subject directory which contains bvals, bvecs, data,\
            and nodif_brain_mask files.
        num_fibres: Number of fibres per voxel (default 3).
        ard_weight: ARD weight, more weight means less secondary fibres per\
            voxel (default 1).
        burnin: Burnin period (default 1000).
        num_jumps: Number of jumps (default 1250).
        sample_every: Sample every (default 25).
        model_type: Deconvolution model. 1: with sticks, 2: with sticks with a\
            range of diffusivities (default), 3: with zeppelins.
        grad_nonlinear: Consider gradient nonlinearities, expects grad_dev in\
            the subject directory.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "bedpostx",
        "subject_dir": subject_dir,
        "grad_nonlinear": grad_nonlinear,
    }
    if num_fibres is not None:
        params["num_fibres"] = num_fibres
    if ard_weight is not None:
        params["ard_weight"] = ard_weight
    if burnin is not None:
        params["burnin"] = burnin
    if num_jumps is not None:
        params["num_jumps"] = num_jumps
    if sample_every is not None:
        params["sample_every"] = sample_every
    if model_type is not None:
        params["model_type"] = model_type
    return params


def bedpostx_cargs(
    params: BedpostxParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("bedpostx")
    cargs.append(params.get("subject_dir"))
    if params.get("num_fibres") is not None:
        cargs.extend([
            "-n",
            str(params.get("num_fibres"))
        ])
    if params.get("ard_weight") is not None:
        cargs.extend([
            "-w",
            str(params.get("ard_weight"))
        ])
    if params.get("burnin") is not None:
        cargs.extend([
            "-b",
            str(params.get("burnin"))
        ])
    if params.get("num_jumps") is not None:
        cargs.extend([
            "-j",
            str(params.get("num_jumps"))
        ])
    if params.get("sample_every") is not None:
        cargs.extend([
            "-s",
            str(params.get("sample_every"))
        ])
    if params.get("model_type") is not None:
        cargs.extend([
            "-model",
            str(params.get("model_type"))
        ])
    if params.get("grad_nonlinear"):
        cargs.append("-g")
    return cargs


def bedpostx_outputs(
    params: BedpostxParameters,
    execution: Execution,
) -> BedpostxOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = BedpostxOutputs(
        root=execution.output_file("."),
        xfms_output=execution.output_file(params.get("subject_dir") + "_bedpostx/xfms/*"),
        diff_slices_output=execution.output_file(params.get("subject_dir") + "_bedpostx/diff_slices/*"),
    )
    return ret


def bedpostx_execute(
    params: BedpostxParameters,
    execution: Execution,
) -> BedpostxOutputs:
    """
    Bayesian Estimation of Diffusion Parameters Obtained using Sampling Techniques
    (BEDPOST) for modeling multiple fibers per voxel.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `BedpostxOutputs`).
    """
    params = execution.params(params)
    cargs = bedpostx_cargs(params, execution)
    ret = bedpostx_outputs(params, execution)
    execution.run(cargs)
    return ret


def bedpostx(
    subject_dir: str,
    num_fibres: float | None = 3,
    ard_weight: float | None = 1,
    burnin: float | None = 1000,
    num_jumps: float | None = 1250,
    sample_every: float | None = 25,
    model_type: float | None = 2,
    grad_nonlinear: bool = False,
    runner: Runner | None = None,
) -> BedpostxOutputs:
    """
    Bayesian Estimation of Diffusion Parameters Obtained using Sampling Techniques
    (BEDPOST) for modeling multiple fibers per voxel.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        subject_dir: Input subject directory which contains bvals, bvecs, data,\
            and nodif_brain_mask files.
        num_fibres: Number of fibres per voxel (default 3).
        ard_weight: ARD weight, more weight means less secondary fibres per\
            voxel (default 1).
        burnin: Burnin period (default 1000).
        num_jumps: Number of jumps (default 1250).
        sample_every: Sample every (default 25).
        model_type: Deconvolution model. 1: with sticks, 2: with sticks with a\
            range of diffusivities (default), 3: with zeppelins.
        grad_nonlinear: Consider gradient nonlinearities, expects grad_dev in\
            the subject directory.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BedpostxOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BEDPOSTX_METADATA)
    params = bedpostx_params(
        subject_dir=subject_dir,
        num_fibres=num_fibres,
        ard_weight=ard_weight,
        burnin=burnin,
        num_jumps=num_jumps,
        sample_every=sample_every,
        model_type=model_type,
        grad_nonlinear=grad_nonlinear,
    )
    return bedpostx_execute(params, execution)


__all__ = [
    "BEDPOSTX_METADATA",
    "BedpostxOutputs",
    "BedpostxParameters",
    "bedpostx",
    "bedpostx_params",
]

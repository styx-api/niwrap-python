# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

BEDPOSTX_MGH_METADATA = Metadata(
    id="3ed864ec81d1c034c4ff17b4f55cad7b918d2d91.boutiques",
    name="bedpostx_mgh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


BedpostxMghParameters = typing.TypedDict('BedpostxMghParameters', {
    "__STYXTYPE__": typing.Literal["bedpostx_mgh"],
    "subject_directory": str,
    "fibres": typing.NotRequired[float | None],
    "ard_weight": typing.NotRequired[float | None],
    "burnin": typing.NotRequired[float | None],
    "jumps": typing.NotRequired[float | None],
    "sample_every": typing.NotRequired[float | None],
    "deconv_model": typing.NotRequired[float | None],
    "gradient_nonlin": bool,
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
        "bedpostx_mgh": bedpostx_mgh_cargs,
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
    }.get(t)


class BedpostxMghOutputs(typing.NamedTuple):
    """
    Output object returned when calling `bedpostx_mgh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def bedpostx_mgh_params(
    subject_directory: str,
    fibres: float | None = None,
    ard_weight: float | None = None,
    burnin: float | None = None,
    jumps: float | None = None,
    sample_every: float | None = None,
    deconv_model: float | None = None,
    gradient_nonlin: bool = False,
) -> BedpostxMghParameters:
    """
    Build parameters.
    
    Args:
        subject_directory: Subject directory containing necessary files such as\
            bvals, bvecs, data, and nodif_brain_mask.
        fibres: Number of fibres per voxel, default is 3.
        ard_weight: ARD weight, more weight means fewer secondary fibres per\
            voxel, default is 1.
        burnin: Burnin period, default is 1000.
        jumps: Number of jumps, default is 1250.
        sample_every: Sample every n steps, default is 25.
        deconv_model: Deconvolution model selection. 1: with sticks, 2: with\
            sticks with a range of diffusivities (default), 3: with zeppelins.
        gradient_nonlin: Consider gradient nonlinearities, default is off.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "bedpostx_mgh",
        "subject_directory": subject_directory,
        "gradient_nonlin": gradient_nonlin,
    }
    if fibres is not None:
        params["fibres"] = fibres
    if ard_weight is not None:
        params["ard_weight"] = ard_weight
    if burnin is not None:
        params["burnin"] = burnin
    if jumps is not None:
        params["jumps"] = jumps
    if sample_every is not None:
        params["sample_every"] = sample_every
    if deconv_model is not None:
        params["deconv_model"] = deconv_model
    return params


def bedpostx_mgh_cargs(
    params: BedpostxMghParameters,
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
    cargs.append("bedpostx_mgh")
    cargs.append(params.get("subject_directory"))
    if params.get("fibres") is not None:
        cargs.extend([
            "-n",
            str(params.get("fibres"))
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
    if params.get("jumps") is not None:
        cargs.extend([
            "-j",
            str(params.get("jumps"))
        ])
    if params.get("sample_every") is not None:
        cargs.extend([
            "-s",
            str(params.get("sample_every"))
        ])
    if params.get("deconv_model") is not None:
        cargs.extend([
            "-model",
            str(params.get("deconv_model"))
        ])
    if params.get("gradient_nonlin"):
        cargs.append("-g")
    return cargs


def bedpostx_mgh_outputs(
    params: BedpostxMghParameters,
    execution: Execution,
) -> BedpostxMghOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = BedpostxMghOutputs(
        root=execution.output_file("."),
    )
    return ret


def bedpostx_mgh_execute(
    params: BedpostxMghParameters,
    execution: Execution,
) -> BedpostxMghOutputs:
    """
    A modified version of FSL's bedpostx compatible with PBS queueing system for
    parallel computation.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `BedpostxMghOutputs`).
    """
    params = execution.params(params)
    cargs = bedpostx_mgh_cargs(params, execution)
    ret = bedpostx_mgh_outputs(params, execution)
    execution.run(cargs)
    return ret


def bedpostx_mgh(
    subject_directory: str,
    fibres: float | None = None,
    ard_weight: float | None = None,
    burnin: float | None = None,
    jumps: float | None = None,
    sample_every: float | None = None,
    deconv_model: float | None = None,
    gradient_nonlin: bool = False,
    runner: Runner | None = None,
) -> BedpostxMghOutputs:
    """
    A modified version of FSL's bedpostx compatible with PBS queueing system for
    parallel computation.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject_directory: Subject directory containing necessary files such as\
            bvals, bvecs, data, and nodif_brain_mask.
        fibres: Number of fibres per voxel, default is 3.
        ard_weight: ARD weight, more weight means fewer secondary fibres per\
            voxel, default is 1.
        burnin: Burnin period, default is 1000.
        jumps: Number of jumps, default is 1250.
        sample_every: Sample every n steps, default is 25.
        deconv_model: Deconvolution model selection. 1: with sticks, 2: with\
            sticks with a range of diffusivities (default), 3: with zeppelins.
        gradient_nonlin: Consider gradient nonlinearities, default is off.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BedpostxMghOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BEDPOSTX_MGH_METADATA)
    params = bedpostx_mgh_params(
        subject_directory=subject_directory,
        fibres=fibres,
        ard_weight=ard_weight,
        burnin=burnin,
        jumps=jumps,
        sample_every=sample_every,
        deconv_model=deconv_model,
        gradient_nonlin=gradient_nonlin,
    )
    return bedpostx_mgh_execute(params, execution)


__all__ = [
    "BEDPOSTX_MGH_METADATA",
    "BedpostxMghOutputs",
    "BedpostxMghParameters",
    "bedpostx_mgh",
    "bedpostx_mgh_params",
]

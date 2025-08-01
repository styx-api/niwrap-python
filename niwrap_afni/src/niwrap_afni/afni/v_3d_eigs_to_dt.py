# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_EIGS_TO_DT_METADATA = Metadata(
    id="2a859820023438ce7134628316920f709603fea4.boutiques",
    name="3dEigsToDT",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dEigsToDtParameters = typing.TypedDict('V3dEigsToDtParameters', {
    "__STYXTYPE__": typing.Literal["3dEigsToDT"],
    "eig_vals": str,
    "eig_vecs": str,
    "prefix": str,
    "mask": typing.NotRequired[InputPathType | None],
    "flip_x": bool,
    "flip_y": bool,
    "flip_z": bool,
    "scale_eigs": typing.NotRequired[float | None],
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
        "3dEigsToDT": v_3d_eigs_to_dt_cargs,
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
        "3dEigsToDT": v_3d_eigs_to_dt_outputs,
    }.get(t)


class V3dEigsToDtOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_eigs_to_dt(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    dt_brik_output: OutputPathType
    """Output diffusion tensor (DT) file in AFNI format (BRIK)"""
    dt_head_output: OutputPathType
    """Output diffusion tensor (DT) file in AFNI format (HEAD)"""


def v_3d_eigs_to_dt_params(
    eig_vals: str,
    eig_vecs: str,
    prefix: str,
    mask: InputPathType | None = None,
    flip_x: bool = False,
    flip_y: bool = False,
    flip_z: bool = False,
    scale_eigs: float | None = None,
) -> V3dEigsToDtParameters:
    """
    Build parameters.
    
    Args:
        eig_vals: Searchable descriptor for finding all three required\
            eigenvalue files. It should list all three eigenvalue files in\
            descending order of magnitude.
        eig_vecs: Searchable descriptor for finding all three required\
            eigenvector files. It should list all three eigenvector files in order\
            matching the eigenvalue files.
        prefix: Prefix for the output file name. It is recommended to include a\
            'DT' label in it.
        mask: Optional mask within which to calculate uncertainty. If not\
            provided, the data should be masked already.
        flip_x: Change sign of the first element of eigenvectors.
        flip_y: Change sign of the second element of eigenvectors.
        flip_z: Change sign of the third element of eigenvectors.
        scale_eigs: Rescale the eigenvalues by dividing by a number X > 0.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dEigsToDT",
        "eig_vals": eig_vals,
        "eig_vecs": eig_vecs,
        "prefix": prefix,
        "flip_x": flip_x,
        "flip_y": flip_y,
        "flip_z": flip_z,
    }
    if mask is not None:
        params["mask"] = mask
    if scale_eigs is not None:
        params["scale_eigs"] = scale_eigs
    return params


def v_3d_eigs_to_dt_cargs(
    params: V3dEigsToDtParameters,
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
    cargs.append("3dEigsToDT")
    cargs.extend([
        "-eig_vals",
        params.get("eig_vals")
    ])
    cargs.extend([
        "-eig_vecs",
        params.get("eig_vecs")
    ])
    cargs.extend([
        "-prefix",
        params.get("prefix")
    ])
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("flip_x"):
        cargs.append("-flip_x")
    if params.get("flip_y"):
        cargs.append("-flip_y")
    if params.get("flip_z"):
        cargs.append("-flip_z")
    if params.get("scale_eigs") is not None:
        cargs.extend([
            "-scale_eigs",
            str(params.get("scale_eigs"))
        ])
    return cargs


def v_3d_eigs_to_dt_outputs(
    params: V3dEigsToDtParameters,
    execution: Execution,
) -> V3dEigsToDtOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dEigsToDtOutputs(
        root=execution.output_file("."),
        dt_brik_output=execution.output_file(params.get("prefix") + "_DT+orig.BRIK"),
        dt_head_output=execution.output_file(params.get("prefix") + "_DT+orig.HEAD"),
    )
    return ret


def v_3d_eigs_to_dt_execute(
    params: V3dEigsToDtParameters,
    execution: Execution,
) -> V3dEigsToDtOutputs:
    """
    Convert set of DTI eigenvectors and eigenvalues to a diffusion tensor, with
    optional value-scaling and vector-flipping.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dEigsToDtOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_eigs_to_dt_cargs(params, execution)
    ret = v_3d_eigs_to_dt_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_eigs_to_dt(
    eig_vals: str,
    eig_vecs: str,
    prefix: str,
    mask: InputPathType | None = None,
    flip_x: bool = False,
    flip_y: bool = False,
    flip_z: bool = False,
    scale_eigs: float | None = None,
    runner: Runner | None = None,
) -> V3dEigsToDtOutputs:
    """
    Convert set of DTI eigenvectors and eigenvalues to a diffusion tensor, with
    optional value-scaling and vector-flipping.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        eig_vals: Searchable descriptor for finding all three required\
            eigenvalue files. It should list all three eigenvalue files in\
            descending order of magnitude.
        eig_vecs: Searchable descriptor for finding all three required\
            eigenvector files. It should list all three eigenvector files in order\
            matching the eigenvalue files.
        prefix: Prefix for the output file name. It is recommended to include a\
            'DT' label in it.
        mask: Optional mask within which to calculate uncertainty. If not\
            provided, the data should be masked already.
        flip_x: Change sign of the first element of eigenvectors.
        flip_y: Change sign of the second element of eigenvectors.
        flip_z: Change sign of the third element of eigenvectors.
        scale_eigs: Rescale the eigenvalues by dividing by a number X > 0.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dEigsToDtOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_EIGS_TO_DT_METADATA)
    params = v_3d_eigs_to_dt_params(
        eig_vals=eig_vals,
        eig_vecs=eig_vecs,
        prefix=prefix,
        mask=mask,
        flip_x=flip_x,
        flip_y=flip_y,
        flip_z=flip_z,
        scale_eigs=scale_eigs,
    )
    return v_3d_eigs_to_dt_execute(params, execution)


__all__ = [
    "V3dEigsToDtOutputs",
    "V3dEigsToDtParameters",
    "V_3D_EIGS_TO_DT_METADATA",
    "v_3d_eigs_to_dt",
    "v_3d_eigs_to_dt_params",
]

# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_DTEIG_METADATA = Metadata(
    id="36a3abb6b11f17e33956cdaa9d15a0c2d499739b.boutiques",
    name="3dDTeig",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dDteigParameters = typing.TypedDict('V3dDteigParameters', {
    "__STYXTYPE__": typing.Literal["3dDTeig"],
    "input_dataset": str,
    "prefix": typing.NotRequired[str | None],
    "datum": typing.NotRequired[typing.Literal["byte", "short", "float"] | None],
    "sep_dsets": bool,
    "uddata": bool,
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
        "3dDTeig": v_3d_dteig_cargs,
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
        "3dDTeig": v_3d_dteig_outputs,
    }.get(t)


class V3dDteigOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_dteig(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_dataset: OutputPathType | None
    """Output dataset with computed eigenvalues, eigenvectors, FA, and MD"""
    output_lambda: OutputPathType | None
    """Output dataset for eigenvalues"""
    output_eigvec: OutputPathType | None
    """Output dataset for eigenvectors"""
    output_fa: OutputPathType | None
    """Output dataset for fractional anisotropy"""
    output_md: OutputPathType | None
    """Output dataset for mean diffusivity"""


def v_3d_dteig_params(
    input_dataset: str,
    prefix: str | None = None,
    datum: typing.Literal["byte", "short", "float"] | None = None,
    sep_dsets: bool = False,
    uddata: bool = False,
) -> V3dDteigParameters:
    """
    Build parameters.
    
    Args:
        input_dataset: Input dataset of Dxx, Dxy, Dyy, Dxz, Dyz, Dzz sub-bricks.
        prefix: Use the given prefix for the output dataset.
        datum: Coerce the output data to be stored as the given type (byte,\
            short, or float).
        sep_dsets: Save eigenvalues, vectors, FA, and MD in separate datasets.
        uddata: Tensor data is stored as upper diagonal instead of lower\
            diagonal.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dDTeig",
        "input_dataset": input_dataset,
        "sep_dsets": sep_dsets,
        "uddata": uddata,
    }
    if prefix is not None:
        params["prefix"] = prefix
    if datum is not None:
        params["datum"] = datum
    return params


def v_3d_dteig_cargs(
    params: V3dDteigParameters,
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
    cargs.append("3dDTeig")
    cargs.append(params.get("input_dataset"))
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("datum") is not None:
        cargs.extend([
            "-datum",
            params.get("datum")
        ])
    if params.get("sep_dsets"):
        cargs.append("-sep_dsets")
    if params.get("uddata"):
        cargs.append("-uddata")
    return cargs


def v_3d_dteig_outputs(
    params: V3dDteigParameters,
    execution: Execution,
) -> V3dDteigOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dDteigOutputs(
        root=execution.output_file("."),
        output_dataset=execution.output_file(params.get("prefix") + ".nii.gz") if (params.get("prefix") is not None) else None,
        output_lambda=execution.output_file(params.get("prefix") + "_lambda.nii.gz") if (params.get("prefix") is not None) else None,
        output_eigvec=execution.output_file(params.get("prefix") + "_eigvec.nii.gz") if (params.get("prefix") is not None) else None,
        output_fa=execution.output_file(params.get("prefix") + "_FA.nii.gz") if (params.get("prefix") is not None) else None,
        output_md=execution.output_file(params.get("prefix") + "_MD.nii.gz") if (params.get("prefix") is not None) else None,
    )
    return ret


def v_3d_dteig_execute(
    params: V3dDteigParameters,
    execution: Execution,
) -> V3dDteigOutputs:
    """
    Computes eigenvalues and eigenvectors for an input dataset of tensors.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dDteigOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_dteig_cargs(params, execution)
    ret = v_3d_dteig_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_dteig(
    input_dataset: str,
    prefix: str | None = None,
    datum: typing.Literal["byte", "short", "float"] | None = None,
    sep_dsets: bool = False,
    uddata: bool = False,
    runner: Runner | None = None,
) -> V3dDteigOutputs:
    """
    Computes eigenvalues and eigenvectors for an input dataset of tensors.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_dataset: Input dataset of Dxx, Dxy, Dyy, Dxz, Dyz, Dzz sub-bricks.
        prefix: Use the given prefix for the output dataset.
        datum: Coerce the output data to be stored as the given type (byte,\
            short, or float).
        sep_dsets: Save eigenvalues, vectors, FA, and MD in separate datasets.
        uddata: Tensor data is stored as upper diagonal instead of lower\
            diagonal.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dDteigOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_DTEIG_METADATA)
    params = v_3d_dteig_params(
        input_dataset=input_dataset,
        prefix=prefix,
        datum=datum,
        sep_dsets=sep_dsets,
        uddata=uddata,
    )
    return v_3d_dteig_execute(params, execution)


__all__ = [
    "V3dDteigOutputs",
    "V3dDteigParameters",
    "V_3D_DTEIG_METADATA",
    "v_3d_dteig",
    "v_3d_dteig_params",
]

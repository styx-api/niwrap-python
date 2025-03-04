# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__CLUST_EXP_CAT_LAB_METADATA = Metadata(
    id="e3acc2b13b06a35c413b7c5aede3d8651316dbe3.boutiques",
    name="@ClustExp_CatLab",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


VClustExpCatLabParameters = typing.TypedDict('VClustExpCatLabParameters', {
    "__STYX_TYPE__": typing.Literal["@ClustExp_CatLab"],
    "prefix": str,
    "input_file": InputPathType,
    "help": bool,
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
        "@ClustExp_CatLab": v__clust_exp_cat_lab_cargs,
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
        "@ClustExp_CatLab": v__clust_exp_cat_lab_outputs,
    }.get(t)


class VClustExpCatLabOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__clust_exp_cat_lab(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output data set concatenating labeled subbriks"""


def v__clust_exp_cat_lab_params(
    prefix: str,
    input_file: InputPathType,
    help_: bool = False,
) -> VClustExpCatLabParameters:
    """
    Build parameters.
    
    Args:
        prefix: Output file name.
        input_file: Name of file containing the labels and data sets table\
            (e.g. subjects.csv).
        help_: Show help information.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@ClustExp_CatLab",
        "prefix": prefix,
        "input_file": input_file,
        "help": help_,
    }
    return params


def v__clust_exp_cat_lab_cargs(
    params: VClustExpCatLabParameters,
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
    cargs.append("@ClustExp_CatLab")
    cargs.extend([
        "-prefix",
        params.get("prefix")
    ])
    cargs.extend([
        "-input",
        execution.input_file(params.get("input_file"))
    ])
    if params.get("help"):
        cargs.append("-help")
    return cargs


def v__clust_exp_cat_lab_outputs(
    params: VClustExpCatLabParameters,
    execution: Execution,
) -> VClustExpCatLabOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VClustExpCatLabOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("prefix") + ".nii.gz"),
    )
    return ret


def v__clust_exp_cat_lab_execute(
    params: VClustExpCatLabParameters,
    execution: Execution,
) -> VClustExpCatLabOutputs:
    """
    Helper script to concatenate and label a group of data sets.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VClustExpCatLabOutputs`).
    """
    params = execution.params(params)
    cargs = v__clust_exp_cat_lab_cargs(params, execution)
    ret = v__clust_exp_cat_lab_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__clust_exp_cat_lab(
    prefix: str,
    input_file: InputPathType,
    help_: bool = False,
    runner: Runner | None = None,
) -> VClustExpCatLabOutputs:
    """
    Helper script to concatenate and label a group of data sets.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        prefix: Output file name.
        input_file: Name of file containing the labels and data sets table\
            (e.g. subjects.csv).
        help_: Show help information.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VClustExpCatLabOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__CLUST_EXP_CAT_LAB_METADATA)
    params = v__clust_exp_cat_lab_params(
        prefix=prefix,
        input_file=input_file,
        help_=help_,
    )
    return v__clust_exp_cat_lab_execute(params, execution)


__all__ = [
    "VClustExpCatLabOutputs",
    "VClustExpCatLabParameters",
    "V__CLUST_EXP_CAT_LAB_METADATA",
    "v__clust_exp_cat_lab",
    "v__clust_exp_cat_lab_params",
]

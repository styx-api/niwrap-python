# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

ADJUNCT_SUMA_FS_MASK_AND_QC_METADATA = Metadata(
    id="a5fd3e30999988458acf431df9f21ab685cbbe45.boutiques",
    name="adjunct_suma_fs_mask_and_qc",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


AdjunctSumaFsMaskAndQcParameters = typing.TypedDict('AdjunctSumaFsMaskAndQcParameters', {
    "__STYX_TYPE__": typing.Literal["adjunct_suma_fs_mask_and_qc"],
    "subj_id": str,
    "suma_dir": str,
    "no_clean": bool,
    "help": bool,
    "hview": bool,
    "version": bool,
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
        "adjunct_suma_fs_mask_and_qc": adjunct_suma_fs_mask_and_qc_cargs,
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
        "adjunct_suma_fs_mask_and_qc": adjunct_suma_fs_mask_and_qc_outputs,
    }.get(t)


class AdjunctSumaFsMaskAndQcOutputs(typing.NamedTuple):
    """
    Output object returned when calling `adjunct_suma_fs_mask_and_qc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    fs_parc_wb_mask: OutputPathType
    """Whole brain mask based on the FS parcellation created by this script."""
    qc_image_00: OutputPathType
    """QC image with overlay of brainmask.nii* volume in red and parcellated
    subset in black."""
    qc_image_01: OutputPathType
    """QC image with overlay of fs_parc_wb_mask.nii.gz."""
    qc_image_02: OutputPathType
    """QC image with overlay of tissue segmentations."""
    qc_image_03: OutputPathType
    """QC image with overlay of GM."""
    qc_image_04: OutputPathType
    """QC image with overlay of WM."""
    qc_image_05: OutputPathType
    """QC image with overlay of "2000" atlas parcellation."""


def adjunct_suma_fs_mask_and_qc_params(
    subj_id: str,
    suma_dir: str,
    no_clean: bool = False,
    help_: bool = False,
    hview: bool = False,
    version: bool = False,
) -> AdjunctSumaFsMaskAndQcParameters:
    """
    Build parameters.
    
    Args:
        subj_id: Subject ID.
        suma_dir: SUMA/ directory output by AFNI's @SUMA_Make_Spec_FS.
        no_clean: Do not remove temporary working subdirectory (default: remove\
            it).
        help_: Show help.
        hview: Show help in text editor.
        version: Show version.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "adjunct_suma_fs_mask_and_qc",
        "subj_id": subj_id,
        "suma_dir": suma_dir,
        "no_clean": no_clean,
        "help": help_,
        "hview": hview,
        "version": version,
    }
    return params


def adjunct_suma_fs_mask_and_qc_cargs(
    params: AdjunctSumaFsMaskAndQcParameters,
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
    cargs.append("adjunct_suma_fs_mask_and_qc")
    cargs.extend([
        "-sid",
        params.get("subj_id")
    ])
    cargs.extend([
        "-suma_dir",
        params.get("suma_dir")
    ])
    if params.get("no_clean"):
        cargs.append("-no_clean")
    if params.get("help"):
        cargs.append("-help")
    if params.get("hview"):
        cargs.append("-hview")
    if params.get("version"):
        cargs.append("-ver")
    return cargs


def adjunct_suma_fs_mask_and_qc_outputs(
    params: AdjunctSumaFsMaskAndQcParameters,
    execution: Execution,
) -> AdjunctSumaFsMaskAndQcOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = AdjunctSumaFsMaskAndQcOutputs(
        root=execution.output_file("."),
        fs_parc_wb_mask=execution.output_file("SUMA/fs_parc_wb_mask.nii.gz"),
        qc_image_00=execution.output_file("SUMA/qc_00*.jpg"),
        qc_image_01=execution.output_file("SUMA/qc_01*.jpg"),
        qc_image_02=execution.output_file("SUMA/qc_02*.jpg"),
        qc_image_03=execution.output_file("SUMA/qc_03*.jpg"),
        qc_image_04=execution.output_file("SUMA/qc_04*.jpg"),
        qc_image_05=execution.output_file("SUMA/qc_05*.jpg"),
    )
    return ret


def adjunct_suma_fs_mask_and_qc_execute(
    params: AdjunctSumaFsMaskAndQcParameters,
    execution: Execution,
) -> AdjunctSumaFsMaskAndQcOutputs:
    """
    Script for quickly making some QC images for the SUMA/ directory created by
    @SUMA_Make_Spec_FS after running FreeSurfer's recon-all.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `AdjunctSumaFsMaskAndQcOutputs`).
    """
    params = execution.params(params)
    cargs = adjunct_suma_fs_mask_and_qc_cargs(params, execution)
    ret = adjunct_suma_fs_mask_and_qc_outputs(params, execution)
    execution.run(cargs)
    return ret


def adjunct_suma_fs_mask_and_qc(
    subj_id: str,
    suma_dir: str,
    no_clean: bool = False,
    help_: bool = False,
    hview: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> AdjunctSumaFsMaskAndQcOutputs:
    """
    Script for quickly making some QC images for the SUMA/ directory created by
    @SUMA_Make_Spec_FS after running FreeSurfer's recon-all.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        subj_id: Subject ID.
        suma_dir: SUMA/ directory output by AFNI's @SUMA_Make_Spec_FS.
        no_clean: Do not remove temporary working subdirectory (default: remove\
            it).
        help_: Show help.
        hview: Show help in text editor.
        version: Show version.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AdjunctSumaFsMaskAndQcOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ADJUNCT_SUMA_FS_MASK_AND_QC_METADATA)
    params = adjunct_suma_fs_mask_and_qc_params(
        subj_id=subj_id,
        suma_dir=suma_dir,
        no_clean=no_clean,
        help_=help_,
        hview=hview,
        version=version,
    )
    return adjunct_suma_fs_mask_and_qc_execute(params, execution)


__all__ = [
    "ADJUNCT_SUMA_FS_MASK_AND_QC_METADATA",
    "AdjunctSumaFsMaskAndQcOutputs",
    "AdjunctSumaFsMaskAndQcParameters",
    "adjunct_suma_fs_mask_and_qc",
    "adjunct_suma_fs_mask_and_qc_params",
]
